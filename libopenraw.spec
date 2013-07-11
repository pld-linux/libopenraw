Summary:	A library for decoding RAW images
Summary(pl.UTF-8):	Biblioteka dekodująca obrazy w formacie RAW
Name:		libopenraw
Version:	0.0.9
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	3611d8aea870d25314665ef53093288e
URL:		http://libopenraw.freedesktop.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	gdk-pixbuf2-devel >= 2.0.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if "%{_lib}" != "lib"
%define		libext		%(lib="%{_lib}"; echo ${lib#lib})
%define		pqext		-%{libext}
%else
%define		pqext		%{nil}
%endif

%description
libopenraw is an ongoing project to provide a free software
implementation for camera RAW files decoding. One of the main reason
is that dcraw is not suited for easy integration into applications,
and there is a need for an easy to use API to build free software
digital image processing application.

%description -l pl.UTF-8
libopenraw jest projektem dostarczającym wolnodostępną
implementację dekodera plików w formacie RAW obsługiwanych przez
cyfrowe aparaty fotograficzne. Jednym z głównych powodów powstania
tej biblioteki jest to, że dcraw nie jest przystosowany do łatwej
integracji z aplikacjami, a istnieje potrzeba stworzenia łatwego w
użyciu API do budowy wolnodostępnej aplikacji przetwarzania cyfrowych
obrazów.

%package devel
Summary:	Header files for libopenraw library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libopenraw
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libstdc++-devel

%description devel
Header files for libopenraw library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libopenraw.

%package static
Summary:	Static libopenraw library
Summary(pl.UTF-8):	Statyczna biblioteka libopenraw
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libopenraw library.

%description static -l pl.UTF-8
Statyczna biblioteka libopenraw.

%package gnome
Summary:	Library for decoding RAW images - GTK+/GNOME support
Summary(pl.UTF-8):	Biblioteka dekodująca obrazy w formacie RAW - obsługa GTK+/GNOME
Group:		X11/Libraries
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gdk-pixbuf2 >= 2.0.0
Requires:	%{name} = %{version}-%{release}
Requires:	gdk-pixbuf2 >= 2.0.0
Requires:	glib2 >= 2.0.0

%description gnome
Library for decoding RAW images - GTK+/GNOME support.

%description gnome -l pl.UTF-8
Biblioteka dekodująca obrazy w formacie RAW - obsługa GTK+/GNOME.

%package gnome-devel
Summary:	Header file for libopenrawgnome library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libopenrawgnome
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gnome = %{version}-%{release}
Requires:	gdk-pixbuf2-devel >= 2.0.0
Requires:	glib2-devel >= 2.0.0

%description gnome-devel
Header file for libopenrawgnome library.

%description gnome-devel -l pl.UTF-8
Plik nagłówkowy biblioteki libopenrawgnome.

%package gnome-static
Summary:	Static libopenrawgnome library
Summary(pl.UTF-8):	Statyczna biblioteka libopenrawgnome
Group:		X11/Development/Libraries
Requires:	%{name}-gnome-devel = %{version}-%{release}

%description gnome-static
Static libopenrawgnome library.

%description gnome-static -l pl.UTF-8
Statyczna biblioteka libopenrawgnome.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	V=1

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/*/loaders/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post gnome
/sbin/ldconfig
umask 022
%{_bindir}/gdk-pixbuf-query-loaders%{pqext} --update-cache

%postun gnome
/sbin/ldconfig
umask 022
if [ -x %{_bindir}/gdk-pixbuf-query-loaders%{pqext} ]; then
	%{_bindir}/gdk-pixbuf-query-loaders%{pqext} --update-cache
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libopenraw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenraw.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenraw.so
%{_libdir}/libopenraw.la
%dir %{_includedir}/libopenraw-1.0
%{_includedir}/libopenraw-1.0/libopenraw
%{_pkgconfigdir}/libopenraw-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libopenraw.a

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenrawgnome.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenrawgnome.so.1
%attr(755,root,root) %{_libdir}/gdk-pixbuf-2.0/*/loaders/libopenraw_pixbuf.so

%files gnome-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenrawgnome.so
%{_libdir}/libopenrawgnome.la
%{_includedir}/libopenraw-1.0/libopenraw-gnome
%{_pkgconfigdir}/libopenraw-gnome-1.0.pc

%files gnome-static
%defattr(644,root,root,755)
%{_libdir}/libopenrawgnome.a
