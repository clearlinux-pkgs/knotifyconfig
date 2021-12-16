#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : knotifyconfig
Version  : 5.89.0
Release  : 40
URL      : https://download.kde.org/stable/frameworks/5.89/knotifyconfig-5.89.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.89/knotifyconfig-5.89.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.89/knotifyconfig-5.89.0.tar.xz.sig
Summary  : Configuration system for KNotify
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0
Requires: knotifyconfig-data = %{version}-%{release}
Requires: knotifyconfig-lib = %{version}-%{release}
Requires: knotifyconfig-license = %{version}-%{release}
Requires: knotifyconfig-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcompletion-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : knotifications-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : libcanberra-dev
BuildRequires : phonon-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev

%description
# KNotifyConfig
Configuration dialog for desktop notifications
## Introduction
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application.

%package data
Summary: data components for the knotifyconfig package.
Group: Data

%description data
data components for the knotifyconfig package.


%package dev
Summary: dev components for the knotifyconfig package.
Group: Development
Requires: knotifyconfig-lib = %{version}-%{release}
Requires: knotifyconfig-data = %{version}-%{release}
Provides: knotifyconfig-devel = %{version}-%{release}
Requires: knotifyconfig = %{version}-%{release}

%description dev
dev components for the knotifyconfig package.


%package lib
Summary: lib components for the knotifyconfig package.
Group: Libraries
Requires: knotifyconfig-data = %{version}-%{release}
Requires: knotifyconfig-license = %{version}-%{release}

%description lib
lib components for the knotifyconfig package.


%package license
Summary: license components for the knotifyconfig package.
Group: Default

%description license
license components for the knotifyconfig package.


%package locales
Summary: locales components for the knotifyconfig package.
Group: Default

%description locales
locales components for the knotifyconfig package.


%prep
%setup -q -n knotifyconfig-5.89.0
cd %{_builddir}/knotifyconfig-5.89.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639697497
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1639697497
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knotifyconfig
cp %{_builddir}/knotifyconfig-5.89.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/knotifyconfig/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/knotifyconfig-5.89.0/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/knotifyconfig/20079e8f79713dce80ab09774505773c926afa2a
pushd clr-build
%make_install
popd
%find_lang knotifyconfig5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/knotifyconfig.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KNotifyConfig/KNotifyConfigWidget
/usr/include/KF5/KNotifyConfig/knotifyconfig_export.h
/usr/include/KF5/KNotifyConfig/knotifyconfigwidget.h
/usr/include/KF5/knotifyconfig_version.h
/usr/lib64/cmake/KF5NotifyConfig/KF5NotifyConfigConfig.cmake
/usr/lib64/cmake/KF5NotifyConfig/KF5NotifyConfigConfigVersion.cmake
/usr/lib64/cmake/KF5NotifyConfig/KF5NotifyConfigTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5NotifyConfig/KF5NotifyConfigTargets.cmake
/usr/lib64/libKF5NotifyConfig.so
/usr/lib64/qt5/mkspecs/modules/qt_KNotifyConfig.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5NotifyConfig.so.5
/usr/lib64/libKF5NotifyConfig.so.5.89.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/knotifyconfig/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/knotifyconfig/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files locales -f knotifyconfig5.lang
%defattr(-,root,root,-)

