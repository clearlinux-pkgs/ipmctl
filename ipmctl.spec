#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipmctl
Version  : 02.00.00.3852
Release  : 76
URL      : https://github.com/intel/ipmctl/archive/v02.00.00.3852/ipmctl-02.00.00.3852.tar.gz
Source0  : https://github.com/intel/ipmctl/archive/v02.00.00.3852/ipmctl-02.00.00.3852.tar.gz
Summary  : Manage Intel DC Optane persistent memory modules
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT
Requires: ipmctl-bin = %{version}-%{release}
Requires: ipmctl-data = %{version}-%{release}
Requires: ipmctl-lib = %{version}-%{release}
Requires: ipmctl-license = %{version}-%{release}
Requires: ipmctl-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libndctl)
BuildRequires : pkgconfig(systemd)
BuildRequires : python3

%description
Oniguruma  ----   (C) K.Kosako <sndgk393 AT ybb DOT ne DOT jp>
http://www.geocities.jp/kosako3/oniguruma/

%package bin
Summary: bin components for the ipmctl package.
Group: Binaries
Requires: ipmctl-data = %{version}-%{release}
Requires: ipmctl-license = %{version}-%{release}

%description bin
bin components for the ipmctl package.


%package data
Summary: data components for the ipmctl package.
Group: Data

%description data
data components for the ipmctl package.


%package dev
Summary: dev components for the ipmctl package.
Group: Development
Requires: ipmctl-lib = %{version}-%{release}
Requires: ipmctl-bin = %{version}-%{release}
Requires: ipmctl-data = %{version}-%{release}
Provides: ipmctl-devel = %{version}-%{release}
Requires: ipmctl = %{version}-%{release}

%description dev
dev components for the ipmctl package.


%package doc
Summary: doc components for the ipmctl package.
Group: Documentation
Requires: ipmctl-man = %{version}-%{release}

%description doc
doc components for the ipmctl package.


%package lib
Summary: lib components for the ipmctl package.
Group: Libraries
Requires: ipmctl-data = %{version}-%{release}
Requires: ipmctl-license = %{version}-%{release}

%description lib
lib components for the ipmctl package.


%package license
Summary: license components for the ipmctl package.
Group: Default

%description license
license components for the ipmctl package.


%package man
Summary: man components for the ipmctl package.
Group: Default

%description man
man components for the ipmctl package.


%prep
%setup -q -n ipmctl-02.00.00.3852
cd %{_builddir}/ipmctl-02.00.00.3852

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613515176
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DASCIIDOC_BINARY=/usr/bin/asciidoc \
-DA2X_BINARY=/usr/bin/a2x
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1613515176
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipmctl
cp %{_builddir}/ipmctl-02.00.00.3852/BaseTools/License.txt %{buildroot}/usr/share/package-licenses/ipmctl/716291b5f2b61d3f09e8695d22dc8b539d8c9648
cp %{_builddir}/ipmctl-02.00.00.3852/BaseTools/Source/C/BrotliCompress/LICENSE %{buildroot}/usr/share/package-licenses/ipmctl/c045813a6c514f2d30d60a07c6aaf3603850e608
cp %{_builddir}/ipmctl-02.00.00.3852/LICENSE %{buildroot}/usr/share/package-licenses/ipmctl/e21a52856139a98b41da616f662889335fb1eea4
cp %{_builddir}/ipmctl-02.00.00.3852/MdeModulePkg/Library/BrotliCustomDecompressLib/LICENSE %{buildroot}/usr/share/package-licenses/ipmctl/c045813a6c514f2d30d60a07c6aaf3603850e608
cp %{_builddir}/ipmctl-02.00.00.3852/MdeModulePkg/License.txt %{buildroot}/usr/share/package-licenses/ipmctl/302141e29032602914e0d986c783ff1c83619b10
cp %{_builddir}/ipmctl-02.00.00.3852/MdeModulePkg/Universal/RegularExpressionDxe/Oniguruma/COPYING %{buildroot}/usr/share/package-licenses/ipmctl/b0d64f0b0dd0585917fbead12758d45912c962ce
cp %{_builddir}/ipmctl-02.00.00.3852/MdePkg/License.txt %{buildroot}/usr/share/package-licenses/ipmctl/302141e29032602914e0d986c783ff1c83619b10
cp %{_builddir}/ipmctl-02.00.00.3852/ShellPkg/License.txt %{buildroot}/usr/share/package-licenses/ipmctl/302141e29032602914e0d986c783ff1c83619b10
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/etc/logrotate.d/ipmctl

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipmctl

%files data
%defattr(-,root,root,-)
/usr/share/ipmctl/ipmctl.conf

%files dev
%defattr(-,root,root,-)
/usr/include/NvmSharedDefs.h
/usr/include/export_api.h
/usr/include/nvm_management.h
/usr/include/nvm_types.h
/usr/lib64/libipmctl.so
/usr/lib64/pkgconfig/libipmctl.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/ipmctl/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libipmctl.so.4
/usr/lib64/libipmctl.so.4.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipmctl/302141e29032602914e0d986c783ff1c83619b10
/usr/share/package-licenses/ipmctl/716291b5f2b61d3f09e8695d22dc8b539d8c9648
/usr/share/package-licenses/ipmctl/b0d64f0b0dd0585917fbead12758d45912c962ce
/usr/share/package-licenses/ipmctl/c045813a6c514f2d30d60a07c6aaf3603850e608
/usr/share/package-licenses/ipmctl/e21a52856139a98b41da616f662889335fb1eea4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ipmctl-change-preferences.1.gz
/usr/share/man/man1/ipmctl-change-sensor.1.gz
/usr/share/man/man1/ipmctl-create-goal.1.gz
/usr/share/man/man1/ipmctl-delete-goal.1.gz
/usr/share/man/man1/ipmctl-delete-pcd.1.gz
/usr/share/man/man1/ipmctl-dump-debug-log.1.gz
/usr/share/man/man1/ipmctl-dump-goal.1.gz
/usr/share/man/man1/ipmctl-dump-session.1.gz
/usr/share/man/man1/ipmctl-dump-support-data.1.gz
/usr/share/man/man1/ipmctl-help.1.gz
/usr/share/man/man1/ipmctl-inject-error.1.gz
/usr/share/man/man1/ipmctl-load-goal.1.gz
/usr/share/man/man1/ipmctl-load-session.1.gz
/usr/share/man/man1/ipmctl-modify-device.1.gz
/usr/share/man/man1/ipmctl-show-acpi.1.gz
/usr/share/man/man1/ipmctl-show-cap.1.gz
/usr/share/man/man1/ipmctl-show-cel.1.gz
/usr/share/man/man1/ipmctl-show-device.1.gz
/usr/share/man/man1/ipmctl-show-error-log.1.gz
/usr/share/man/man1/ipmctl-show-firmware.1.gz
/usr/share/man/man1/ipmctl-show-goal.1.gz
/usr/share/man/man1/ipmctl-show-memory-resources.1.gz
/usr/share/man/man1/ipmctl-show-pcd.1.gz
/usr/share/man/man1/ipmctl-show-performance.1.gz
/usr/share/man/man1/ipmctl-show-preferences.1.gz
/usr/share/man/man1/ipmctl-show-region.1.gz
/usr/share/man/man1/ipmctl-show-sensor.1.gz
/usr/share/man/man1/ipmctl-show-session.1.gz
/usr/share/man/man1/ipmctl-show-socket.1.gz
/usr/share/man/man1/ipmctl-show-system-capabilities.1.gz
/usr/share/man/man1/ipmctl-show-topology.1.gz
/usr/share/man/man1/ipmctl-start-diagnostic.1.gz
/usr/share/man/man1/ipmctl-start-session.1.gz
/usr/share/man/man1/ipmctl-stop-session.1.gz
/usr/share/man/man1/ipmctl-update-firmware.1.gz
/usr/share/man/man1/ipmctl-version.1.gz
/usr/share/man/man1/ipmctl.1.gz
