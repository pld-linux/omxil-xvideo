Summary:	X Video display component for Bellagio OpenMAX IL
Summary(pl.UTF-8):	Komponent wyświetlający X Video dla implementacji Bellagio OpenMAX IL
Name:		omxil-xvideo
Version:	0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/omxil/libomxxvideo-%{version}.tar.gz
# Source0-md5:	853c9892f68a14c9a3ff94148701de60
URL:		http://omxil.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libomxil-bellagio-devel >= 0.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXv-devel
Requires:	libomxil-bellagio >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/usr/%{_lib}/bellagio

%description
X Video component is a video display component for Bellagio OpenMAX IL
that uses the Xlib for the visualization.

%description -l pl.UTF-8
Komponent X Video to komponent wyświetlający obraz dla implementacji
Bellagio OpenMAX IL wykorzystujący do wizualizacji bibliotekę Xlib.

%prep
%setup -q -n libomxxvideo-%{version}

%build
# rebuild for as-needed to work
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libomxxvideo.so*
