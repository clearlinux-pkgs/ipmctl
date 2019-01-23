#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipmctl
Version  : 01.00.00.3402
Release  : 14
URL      : https://github.com/intel/ipmctl/archive/v01.00.00.3402.tar.gz
Source0  : https://github.com/intel/ipmctl/archive/v01.00.00.3402.tar.gz
Summary  : Manage Intel DC Optane persistent memory modules
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT
Requires: ipmctl-bin = %{version}-%{release}
Requires: ipmctl-config = %{version}-%{release}
Requires: ipmctl-data = %{version}-%{release}
Requires: ipmctl-lib = %{version}-%{release}
Requires: ipmctl-license = %{version}-%{release}
Requires: ipmctl-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : doxygen
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : libsafec-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libndctl)
BuildRequires : pkgconfig(safec-3.3)
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
Requires: ipmctl-config = %{version}-%{release}
Requires: ipmctl-license = %{version}-%{release}
Requires: ipmctl-services = %{version}-%{release}

%description bin
bin components for the ipmctl package.


%package config
Summary: config components for the ipmctl package.
Group: Default

%description config
config components for the ipmctl package.


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


%package services
Summary: services components for the ipmctl package.
Group: Systemd services

%description services
services components for the ipmctl package.


%prep
%setup -q -n ipmctl-01.00.00.3402

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548204889
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1548204889
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

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipmctl
/usr/bin/ipmctl-monitor

%files config
%defattr(-,root,root,-)
%exclude /usr/etc/logrotate.d/ipmctl.conf

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

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ipmctl-monitor.service
