%define major 0
%define oldlibname %mklibname qaccessibilityclient %{major}
%define libname %mklibname qaccessibilityclient-qt5 %{major}
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
%{_datadir}/qlogging-categories5/libqaccessibilityclient.categories

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
%dir %{_libdir}/cmake/
%{_libdir}/cmake/QAccessibilityClient/
%{_libdir}/libqaccessibilityclient-qt5.so
%{_includedir}/QAccessibilityClient/

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%build
%cmake_qt5 \
	-DQT4_BUILD:BOOL=OFF \
	-DQT5_BUILD:BOOL=ON
cd ..

export CMAKE_BUILD_DIR=build-qt6 
%cmake \
    -DQT_MAJOR_VERSION=6 \
    -G Ninja

%make_build

%make_build -C build-qt6

%install
%make_install -C build

%make_install -C build-qt6

