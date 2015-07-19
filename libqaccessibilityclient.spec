%define major 0
%define libname %mklibname qaccessibilityclient %{major}
%define devname %mklibname qaccessibilityclient -d

Summary:	Accessibility client library for Qt
Name:		libqaccessibilityclient
Version:	0.1.1
Release:	4
License:	LGPLv2+
Group:		System/Libraries
Url:		https://projects.kde.org/projects/playground/accessibility/libkdeaccessibilityclient
Source0:	http://download.kde.org/stable/libqaccessibilityclient/%{name}-%{version}.tar.bz2
Patch0:		qaccessibilityclient-0.1.0-dso.patch
Patch1:		libqaccessibilityclient-0.1.1-QT4_BUILD.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtDBus)
BuildRequires:	pkgconfig(QtGui)

%description
Accessibility client library for Qt.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Accessibility client library for Qt
Group:		System/Libraries

%description -n %{libname}
Accessibility client library for Qt.

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libqaccessibilityclient.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:	qaccessibilityclient-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/qaccessibilityclient/
%dir %{_libdir}/cmake/
%{_libdir}/cmake/QAccessibilityClient/
%{_libdir}/libqaccessibilityclient.so

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .dso
%patch1 -p1 -b .QT4_BUILD

%build
export CC=gcc
export CXX=g++

%cmake_qt4 \
	-DQT4_BUILD:BOOL=ON
%make

%install
%makeinstall_std -C build

## unpackaged files
# consider putting into -tools subpkg?
rm -f %{buildroot}%{_bindir}/accessibleapps

