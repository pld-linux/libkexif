%define		_snap	040920
Summary:	KDE EXIF Data Handling Library 
Summary(pl):	Biblioteka obs³ugi danych z exif w KDE
Name:		libkexif
Version:	0.1.0
Release:	0.%{_snap}1
License:	GPL v2+
Group:		Libraries
# From KDE cvs generated using
# 'cvs://pld/kde/package-kdeapp_snap.sh libkipi kdeextragear-libs-1'
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	c1bd47222e68378cf1931ce2330840b9
URL:		http://webcvs.kde.org/cgi-bin/cvsweb.cgi/kdeextragear-libs-1/libkexif/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	libexif-devel >= 0.6.9
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libkexif is a library for manipulating EXIF information embedded in
images. It currently supports viewing of all EXIF information via
libexif. It also supports the modification of a few attributes in a
safe way that preserves all other EXIF information in the file.

%description -l pl
Libkexif to biblioteka do manipulacji danymi EXIF zawartymi w
obrazach. Aktualnie wspiera podgl±d wszystkich informacji poprzez
libexif oraz modyfikacjê kilku atrybutów przy zachowaniu niezmienno¶ci
pozosta³ych.

%package devel
Summary:	Header files for libkexif development
Summary(pl):	Pliki nag³ówkowe dla programistów u¿ywaj±cych libkexif
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= 9:3.2.0
Requires:	libexif-devel >= 0.6.9

%description devel
Header files for libkexif  development.

%description devel -l pl
Pliki nag³ówkowe dla programistów u¿ywaj±cych libkexif.

%prep
%setup -q -n %{name}

%build
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc libkexif/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_libdir}/lib*.so.?.?.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libkexif
%{_pkgconfigdir}/libkexif.pc
