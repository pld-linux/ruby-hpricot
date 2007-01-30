Summary:	A fast and easy HTML parser
Summary(pl):	Szybki i prosty analizator HTML-a
Name:		ruby-hpricot
Version:	0.4.99
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://code.whytheluckystiff.net/gems/hpricot-%{version}.gem
# Source0-md5:	cb5014d1ad15dbcecd9737787a345ddc
URL:		http://code.whytheluckystiff.net/hpricot/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hpricot is a very flexible HTML parser, based on Tanaka Akira's HTree
and John Resig's JQuery, but with the scanner recoded in C (using
Ragel for scanning.) I've borrowed what I believe to be the best ideas
from these wares to make Hpricot heaps of fun to use.

%description -l pl
Hpricot to bardzo elastyczny analizator HTML-a, oparty na HTree Tanaka
Akiry i JQuery Johna Resiga, ale ze skanerem napisanym w C
(wykorzystuj�cym Ragela). Z tych wyrob�w zapo�yczono najlepsze
pomys�y, aby uczyni� Hpricota najprzyjemniejszym w u�yciu.

%prep
%setup -q -c -n hpricot-%{version}
tar xzf data.tar.gz
cp %{_datadir}/setup.rb .

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

#cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc rdoc
%{ruby_rubylibdir}/hpricot*
%{ruby_archdir}/hpricot*
#%{ruby_ridir}/*
