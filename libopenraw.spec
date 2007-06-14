Summary:	A library for decoding RAW images
Summary(pl.UTF-8):	Biblioteka dekodująca obrazy w formacie RAW
Name:		libopenraw
Version:	0.0.2
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	eae40ecaa92f69d99b27ae3bad8aa8ae
URL:		http://libopenraw.freedesktop.org/
BuildRequires:	boost-bind-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
