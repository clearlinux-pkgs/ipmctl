#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipmctl
Version  : 02.00.00.3689
Release  : 46
URL      : https://github.com/intel/ipmctl/archive/v02.00.00.3689/ipmctl-02.00.00.3689.tar.gz
Source0  : https://github.com/intel/ipmctl/archive/v02.00.00.3689/ipmctl-02.00.00.3689.tar.gz
Summary  : Manage Intel DC Optane persistent memory modules
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT
Requires: ipmctl-bin = %{version}-%{release}
Requires: ipmctl-data = %{version}-%{release}
Requires: ipmctl-lib = %{version}-%{release}
Requires: ipmctl-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : doxygen
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libndctl)
BuildRequires : pkgconfig(systemd)
BuildRequires : python3

%description
### Introduction
Brotli is a generic-purpose lossless compression algorithm that compresses data
using a combination of a modern variant of the LZ77 algorithm, Huffman coding
and 2nd order context modeling, with a compression ratio comparable to the best
currently available general-purpose compression methods. It is similar in speed
with deflate but offers more dense compression.

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
Requires: ipmctl = %{version}-%{release}

%description dev
dev components for the ipmctl package.


%package doc
Summary: doc components for the ipmctl package.
Group: Documentation

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


%prep
%setup -q -n ipmctl-02.00.00.3689
cd %{_builddir}/ipmctl-02.00.00.3689

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578499141
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
export SOURCE_DATE_EPOCH=1578499141
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipmctl
cp %{_builddir}/ipmctl-02.00.00.3689/BaseTools/License.txt %{buildroot}/usr/share/package-licenses/ipmctl/716291b5f2b61d3f09e8695d22dc8b539d8c9648
cp %{_builddir}/ipmctl-02.00.00.3689/BaseTools/Source/C/BrotliCompress/LICENSE %{buildroot}/usr/share/package-licenses/ipmctl/c045813a6c514f2d30d60a07c6aaf3603850e608
cp %{_builddir}/ipmctl-02.00.00.3689/LICENSE %{buildroot}/usr/share/package-licenses/ipmctl/c2401e81d7dc4dd069167ad3a2c7dafeb0eef2e0
cp %{_builddir}/ipmctl-02.00.00.3689/MdeModulePkg/Library/BrotliCustomDecompressLib/LICENSE %{buildroot}/usr/share/package-licenses/ipmctl/c045813a6c514f2d30d60a07c6aaf3603850e608
cp %{_builddir}/ipmctl-02.00.00.3689/MdeModulePkg/License.txt %{buildroot}/usr/share/package-licenses/ipmctl/302141e29032602914e0d986c783ff1c83619b10
cp %{_builddir}/ipmctl-02.00.00.3689/MdeModulePkg/Universal/RegularExpressionDxe/Oniguruma/COPYING %{buildroot}/usr/share/package-licenses/ipmctl/b0d64f0b0dd0585917fbead12758d45912c962ce
cp %{_builddir}/ipmctl-02.00.00.3689/MdePkg/License.txt %{buildroot}/usr/share/package-licenses/ipmctl/302141e29032602914e0d986c783ff1c83619b10
cp %{_builddir}/ipmctl-02.00.00.3689/ShellPkg/License.txt %{buildroot}/usr/share/package-licenses/ipmctl/302141e29032602914e0d986c783ff1c83619b10
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
/usr/share/package-licenses/ipmctl/c2401e81d7dc4dd069167ad3a2c7dafeb0eef2e0
