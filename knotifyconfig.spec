#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : knotifyconfig
Version  : 5.62.0
Release  : 18
URL      : https://download.kde.org/stable/frameworks/5.62/knotifyconfig-5.62.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.62/knotifyconfig-5.62.0.tar.xz
Source1 : https://download.kde.org/stable/frameworks/5.62/knotifyconfig-5.62.0.tar.xz.sig
Summary  : Configuration system for KNotify
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: knotifyconfig-lib = %{version}-%{release}
Requires: knotifyconfig-license = %{version}-%{release}
Requires: knotifyconfig-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kbookmarks-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : knotifications-dev
BuildRequires : kservice-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : phonon-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : solid-dev

%description
# KNotifyConfig
Configuration dialog for desktop notifications
## Introduction
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application.

%package dev
Summary: dev components for the knotifyconfig package.
Group: Development
Requires: knotifyconfig-lib = %{version}-%{release}
Provides: knotifyconfig-devel = %{version}-%{release}
Requires: knotifyconfig = %{version}-%{release}
Requires: knotifyconfig = %{version}-%{release}

%description dev
dev components for the knotifyconfig package.


%package lib
Summary: lib components for the knotifyconfig package.
Group: Libraries
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
%setup -q -n knotifyconfig-5.62.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568935020
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1568935020
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/knotifyconfig
cp COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/knotifyconfig/COPYING.LGPL-2
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/knotifyconfig/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang knotifyconfig5

%files
%defattr(-,root,root,-)

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
/usr/lib64/libKF5NotifyConfig.so.5.62.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/knotifyconfig/COPYING.LGPL-2
/usr/share/package-licenses/knotifyconfig/COPYING.LIB

%files locales -f knotifyconfig5.lang
%defattr(-,root,root,-)

