Summary:	A fast HTML parser
Summary(pl.UTF-8):	Szybki parser HTML-a
Name:		ruby-hpricot
Version:	0.8.6
Release:	8
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/hpricot-%{version}.gem
# Source0-md5:	b0f1f02448037f4f6243c33d5f818fa4
Patch0:		hpricot-ruby34.patch
URL:		https://github.com/hpricot/hpricot
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hpricot is a fast HTML parser, based on a small C-based scanner.

%description -l pl.UTF-8
Hpricot to szybki parser HTML-a, oparty na niewielkim skanerze w C.

%package rdoc
Summary:	HTML documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{name}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4
BuildArch:	noarch

%description rdoc
HTML documentation for %{name}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{name}.

%package ri
Summary:	ri documentation for %{name}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{name}
Group:		Documentation
Requires:	ruby
BuildArch:	noarch

%description ri
ri documentation for %{name}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{name}.

%prep
%setup -q -n hpricot-%{version}
%patch -P0 -p1

%build
cd ext/hpricot_scan
%{__ruby} extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

cd ../fast_xs
%{__ruby} extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

cd ../..
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_vendorarchdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
install -p ext/hpricot_scan/hpricot_scan.so $RPM_BUILD_ROOT%{ruby_vendorarchdir}
install -p ext/fast_xs/fast_xs.so $RPM_BUILD_ROOT%{ruby_vendorarchdir}

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG COPYING
%attr(755,root,root) %{ruby_vendorarchdir}/hpricot_scan.so
%attr(755,root,root) %{ruby_vendorarchdir}/fast_xs.so
%{ruby_vendorlibdir}/hpricot.rb
%{ruby_vendorlibdir}/hpricot

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Hpricot
%{ruby_ridir}/Kernel
%{ruby_ridir}/Object
