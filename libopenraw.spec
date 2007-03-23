#
Summary:	A library for decoding RAW images
Name:		libopenraw
Version:	0.0.2
Release:	1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	eae40ecaa92f69d99b27ae3bad8aa8ae
URL:		http://libopenraw.freedesktop.org/
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libopenraw is an ongoing project to provide a free software
implementation for camera RAW files decoding. One of the main reason
is that [WWW]dcraw is not suited for easy integration into
applications, and there is a need for an easy to use API to build free
software digital image processing application.

%package devel
Summary:	Header files for libopenraw library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libopenraw.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.so
%{_libdir}/*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
