#
# Conditional build:
%bcond_without	tests		# build without tests

%define pkgname hpricot
Summary:	A fast and easy HTML parser
Summary(pl.UTF-8):	Szybki i prosty analizator HTML-a
Name:		ruby-%{pkgname}
Version:	0.8.6
Release:	6
License:	MIT
Group:		Development/Languages
#Source0Download: https://github.com/hpricot/hpricot/releases
Source0:	https://github.com/hpricot/hpricot/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	22cb09304283a1b9590385850bd462c1
URL:		https://rubygems.org/gems/hpricot
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
BuildRequires:	setup.rb >= 3.4.1-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hpricot is a very flexible HTML parser, based on Tanaka Akira's HTree
and John Resig's JQuery, but with the scanner recoded in C (using
Ragel for scanning.) I've borrowed what I believe to be the best ideas
from these wares to make Hpricot heaps of fun to use.

%description -l pl.UTF-8
Hpricot to bardzo elastyczny analizator HTML-a, oparty na HTree Tanaka
Akiry i JQuery Johna Resiga, ale ze skanerem napisanym w C
(wykorzystującym Ragela). Z tych wyrobów zapożyczono najlepsze
pomysły, aby uczynić Hpricota najprzyjemniejszym w użyciu.

%prep
%setup -q -n hpricot-%{version}

cp %{_datadir}/setup.rb .

cd ext/hpricot_scan
ls *.c *.h > MANIFEST

%build
# make gemspec self-contained
ruby -r rubygems -e 'spec = eval(File.read("%{pkgname}.gemspec"))
	File.open("%{pkgname}-%{version}.gemspec", "w") do |file|
	file.puts spec.to_ruby_for_cache
end'

%{__ruby} setup.rb config \
	--rbdir=%{ruby_vendorlibdir} \
	--sodir=%{ruby_vendorarchdir}

%{__ruby} setup.rb setup

%if %{with tests}
%{__ruby} -Ilib -Iext/fast_xs -Iext/hpricot_scan -r hpricot -e 1
%endif

# rdoc crashes on _why's craaazy code.
#rdoc --op rdoc lib
#rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_specdir},%{ruby_ridir}}
%{__ruby} setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

#cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/hpricot.rb
%{ruby_vendorlibdir}/hpricot
%attr(755,root,root) %{ruby_vendorarchdir}/fast_xs.so
%attr(755,root,root) %{ruby_vendorarchdir}/hpricot_scan.so
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
