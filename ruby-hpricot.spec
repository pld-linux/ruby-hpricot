#
# Conditional build:
%bcond_without	tests		# build without tests

Summary:	A fast and easy HTML parser
Summary(pl.UTF-8):	Szybki i prosty analizator HTML-a
Name:		ruby-hpricot
Version:	0.8.2
Release:	4
License:	MIT
Group:		Development/Languages
Source0:	http://github.com/hpricot/hpricot/tarball/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	def40ba2aeb04511df9ec47d3bcecf0e
URL:		http://hpricot.com/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
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
%setup -qc
mv hpricot-hpricot-*/* .

cd ext/hpricot_scan
ls *.c *.h > MANIFEST

%build
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
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}
%{__ruby} setup.rb install \
	--prefix=$RPM_BUILD_ROOT

#cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/hpricot.rb
%{ruby_vendorlibdir}/hpricot
%attr(755,root,root) %{ruby_vendorarchdir}/fast_xs.so
%attr(755,root,root) %{ruby_vendorarchdir}/hpricot_scan.so
