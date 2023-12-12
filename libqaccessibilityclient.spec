%define major 0
%define olderlibname %mklibname qaccessibilityclient %{major}
%define oldlibname %mklibname qaccessibilityclient-qt5 %{major}
%define libname %mklibname qaccessibilityclient-qt5
%define devname %mklibname qaccessibilityclient-qt5 -d
#------------------------------------------------------
%define libqt6name %mklibname qaccessibilityclient-qt6
%define devqt6name %mklibname qaccessibilityclient-qt6 -d

Summary:	Accessibility client library for Qt
Name:		libqaccessibilityclient
Version:	0.6.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://projects.kde.org/projects/playground/accessibility/libkdeaccessibilityclient
Source0:	http://download.kde.org/unstable/libqaccessibilityclient/%{name}-%{version}.tar.xz
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	qmake5
BuildRequires:	qt5-macros
# QT6
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:	qt6-qtbase-theme-gtk3

%description
Accessibility client library for Qt.

%files
%doc AUTHORS README.md
%{_bindir}/dumper

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Accessibility client library for Qt
Group:		System/Libraries
Obsoletes:	%{olderlibname} < %{EVRD}
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n %{libname}
Accessibility client library for Qt.

%files -n %{libname}
%{_libdir}/libqaccessibilityclient-qt5.so.%{major}*
%{_datadir}/qlogging-categories5/libqaccessibilityclient.categories

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:	qaccessibilityclient-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_libdir}/cmake/QAccessibilityClient/
%{_libdir}/libqaccessibilityclient-qt5.so
%{_includedir}/QAccessibilityClient/

#----------------------------------------------------------------------------

%package -n %{libqt6name}
Summary:	Accessibility client library for Qt
Group:		System/Libraries

%description -n %{libqt6name}
Accessibility client library for Qt.

%files -n %{libqt6name}
%{_datadir}/qlogging-categories6/libqaccessibilityclient.categories
%{_libdir}/libqaccessibilityclient-qt6.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devqt6name}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libqt6name} = %{EVRD}
Provides:	qaccessibilityclient-devel = %{EVRD}

%description -n %{devqt6name}
Development files for %{name}.

%files -n %{devqt6name}
%{_libdir}/cmake/QAccessibilityClient6/
%{_libdir}/libqaccessibilityclient-qt6.so
%{_includedir}/QAccessibilityClient6/

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_qt5 \
	-DQT4_BUILD:BOOL=OFF \
	-DQT5_BUILD:BOOL=ON \
	-G Ninja
cd ..

export CMAKE_BUILD_DIR=build-qt6 
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-G Ninja

%build
%ninja_build -C build

%ninja_build -C build-qt6

%install
%ninja_install -C build

%ninja_install -C build-qt6
