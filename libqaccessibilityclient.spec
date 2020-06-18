%define major 0
%define oldlibname %mklibname qaccessibilityclient %{major}
%define libname %mklibname qaccessibilityclient-qt5 %{major}
%define devname %mklibname qaccessibilityclient-qt5 -d

Summary:	Accessibility client library for Qt
Name:		libqaccessibilityclient
Version:	0.4.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://projects.kde.org/projects/playground/accessibility/libkdeaccessibilityclient
Source0:	http://download.kde.org/unstable/libqaccessibilityclient/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	qmake5
BuildRequires:	qt5-macros

%description
Accessibility client library for Qt.

%files
%doc AUTHORS README.md ChangeLog
%license COPYING
%{_bindir}/dumper
%{_bindir}/accessibleapps

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Accessibility client library for Qt
Group:		System/Libraries
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n %{libname}
Accessibility client library for Qt.

%files -n %{libname}
%{_libdir}/libqaccessibilityclient-qt5.so.%{major}*

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
%{_libdir}/libqaccessibilityclient-qt5.so

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake_qt5 \
	-DQT4_BUILD:BOOL=OFF \
	-DQT5_BUILD:BOOL=ON

%make_build

%install
%make_install -C build

