Summary:	KDE EXIF Data Handling Library 
Summary(pl):	Biblioteka obs�ugi danych z exif w KDE
Name:		libkexif
Version:	0.2.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/digikam/%{name}-%{version}.tar.bz2
# Source0-md5:	3adf724e84da04fa0ee6f92ac9516468
URL:		http://digikam.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	libexif-devel >= 0.6.9
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libkexif is a library for manipulating EXIF information embedded in
images. It currently supports viewing of all EXIF information via
libexif. It also supports the modification of a few attributes in a
safe way that preserves all other EXIF information in the file.

%description -l pl
Libkexif to biblioteka do manipulacji danymi EXIF zawartymi w
obrazach. Aktualnie wspiera podgl�d wszystkich informacji poprzez
libexif oraz modyfikacj� kilku atrybut�w przy zachowaniu niezmienno�ci
pozosta�ych.

%package devel
Summary:	Header files for libkexif development
Summary(pl):	Pliki nag��wkowe dla programist�w u�ywaj�cych libkexif
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= 9:3.2.0
Requires:	libexif-devel >= 0.6.9

%description devel
Header files for libkexif  development.

%description devel -l pl
Pliki nag��wkowe dla programist�w u�ywaj�cych libkexif.

%prep
%setup -q

%build
cp -f %{_datadir}/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT/usr/share/locale/is

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.?.?.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libkexif
%{_pkgconfigdir}/libkexif.pc
