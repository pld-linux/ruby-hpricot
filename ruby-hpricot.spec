Summary:	A fast and easy HTML parser
Summary(pl.UTF-8):	Szybki i prosty analizator HTML-a
Name:		ruby-hpricot
Version:	0.8.2
Release:	4
License:	MIT
Group:		Development/Languages
Source0:	http://github.com/hpricot/hpricot/tarball/0.8.2/%{name}-%{version}.tar.gz
# Source0-md5:	def40ba2aeb04511df9ec47d3bcecf0e
URL:		http://hpricot.com/
BuildRequires:	rpmbuild(macros) >= 1.277
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
%setup -q -c
mv hpricot-hpricot-*/* .
rm -rf hpricot-hpricot-*

%build
cd ext/hpricot_scan
ls *.c *.h > MANIFEST
cd ../..
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

# rdoc crashes on _why's craaazy code.
#rdoc --op rdoc lib
#rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

#cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc rdoc
%{ruby_rubylibdir}/hpricot*
%{ruby_archdir}/hpricot*
%{ruby_archdir}/fast_xs.so
#%{ruby_ridir}/*
