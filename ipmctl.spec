#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipmctl
Version  : 02.00.00.3576
Release  : 25
URL      : https://github.com/intel/ipmctl/archive/v02.00.00.3576/ipmctl-02.00.00.3576.tar.gz
Source0  : https://github.com/intel/ipmctl/archive/v02.00.00.3576/ipmctl-02.00.00.3576.tar.gz
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
%setup -q -n ipmctl-02.00.00.3576

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566906586
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
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1566906586
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipmctl
cp BaseTools/License.txt %{buildroot}/usr/share/package-licenses/ipmctl/BaseTools_License.txt
cp BaseTools/Source/C/BrotliCompress/LICENSE %{buildroot}/usr/share/package-licenses/ipmctl/BaseTools_Source_C_BrotliCompress_LICENSE
cp LICENSE %{buildroot}/usr/share/package-licenses/ipmctl/LICENSE
cp MdeModulePkg/Library/BrotliCustomDecompressLib/LICENSE %{buildroot}/usr/share/package-licenses/ipmctl/MdeModulePkg_Library_BrotliCustomDecompressLib_LICENSE
cp MdeModulePkg/License.txt %{buildroot}/usr/share/package-licenses/ipmctl/MdeModulePkg_License.txt
cp MdeModulePkg/Universal/RegularExpressionDxe/Oniguruma/COPYING %{buildroot}/usr/share/package-licenses/ipmctl/MdeModulePkg_Universal_RegularExpressionDxe_Oniguruma_COPYING
cp MdePkg/License.txt %{buildroot}/usr/share/package-licenses/ipmctl/MdePkg_License.txt
cp ShellPkg/License.txt %{buildroot}/usr/share/package-licenses/ipmctl/ShellPkg_License.txt
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/etc/logrotate.d/ipmctl.conf

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
/usr/include/*.h
/usr/lib64/libipmctl.so
/usr/lib64/pkgconfig/libipmctl.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/ipmctl/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libipmctl.so.3
/usr/lib64/libipmctl.so.3.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipmctl/BaseTools_License.txt
/usr/share/package-licenses/ipmctl/BaseTools_Source_C_BrotliCompress_LICENSE
/usr/share/package-licenses/ipmctl/LICENSE
/usr/share/package-licenses/ipmctl/MdeModulePkg_Library_BrotliCustomDecompressLib_LICENSE
/usr/share/package-licenses/ipmctl/MdeModulePkg_License.txt
/usr/share/package-licenses/ipmctl/MdeModulePkg_Universal_RegularExpressionDxe_Oniguruma_COPYING
/usr/share/package-licenses/ipmctl/MdePkg_License.txt
/usr/share/package-licenses/ipmctl/ShellPkg_License.txt
