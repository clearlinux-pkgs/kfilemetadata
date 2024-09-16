#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v19
# autospec commit: f35655a
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kfilemetadata
Version  : 6.6.0
Release  : 102
URL      : https://download.kde.org/stable/frameworks/6.6/kfilemetadata-6.6.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.6/kfilemetadata-6.6.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.6/kfilemetadata-6.6.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : A library for extracting file metadata
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.1 LGPL-3.0
Requires: kfilemetadata-data = %{version}-%{release}
Requires: kfilemetadata-lib = %{version}-%{release}
Requires: kfilemetadata-license = %{version}-%{release}
Requires: kfilemetadata-locales = %{version}-%{release}
BuildRequires : attr-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : exiv2-dev
BuildRequires : extra-cmake-modules pkgconfig(poppler)
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : libkexiv2-dev
BuildRequires : not-ffmpeg-dev
BuildRequires : pkg-config
BuildRequires : poppler-dev
BuildRequires : python3-dev
BuildRequires : qt6base-dev
BuildRequires : taglib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This folder contains various small files to be indexed by indexerextractortests.

%package data
Summary: data components for the kfilemetadata package.
Group: Data

%description data
data components for the kfilemetadata package.


%package dev
Summary: dev components for the kfilemetadata package.
Group: Development
Requires: kfilemetadata-lib = %{version}-%{release}
Requires: kfilemetadata-data = %{version}-%{release}
Provides: kfilemetadata-devel = %{version}-%{release}
Requires: kfilemetadata = %{version}-%{release}

%description dev
dev components for the kfilemetadata package.


%package lib
Summary: lib components for the kfilemetadata package.
Group: Libraries
Requires: kfilemetadata-data = %{version}-%{release}
Requires: kfilemetadata-license = %{version}-%{release}

%description lib
lib components for the kfilemetadata package.


%package license
Summary: license components for the kfilemetadata package.
Group: Default

%description license
license components for the kfilemetadata package.


%package locales
Summary: locales components for the kfilemetadata package.
Group: Default

%description locales
locales components for the kfilemetadata package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kfilemetadata-6.6.0
cd %{_builddir}/kfilemetadata-6.6.0
pushd ..
cp -a kfilemetadata-6.6.0 buildavx2
popd

%build
## build_prepend content
# Make sure the package only builds if karchive has been updated first
sed -i -r -e 's,(KF.? \$\{KF.?_DEP_VERSION\} COMPONENTS Archive)(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726445191
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
# Make sure the package only builds if karchive has been updated first
sed -i -r -e 's,(KF.? \$\{KF.?_DEP_VERSION\} COMPONENTS Archive)(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1726445191
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kfilemetadata
cp %{_builddir}/kfilemetadata-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kfilemetadata/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kfilemetadata-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kfilemetadata/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kfilemetadata-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kfilemetadata/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kfilemetadata-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kfilemetadata/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kfilemetadata-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kfilemetadata/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kfilemetadata-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kfilemetadata/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kfilemetadata-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kfilemetadata/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kfilemetadata6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kfilemetadata.categories
/usr/share/qlogging-categories6/kfilemetadata.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KFileMetaData/KFileMetaData/EmbeddedImageData
/usr/include/KF6/KFileMetaData/KFileMetaData/ExtractionResult
/usr/include/KF6/KFileMetaData/KFileMetaData/Extractor
/usr/include/KF6/KFileMetaData/KFileMetaData/ExtractorCollection
/usr/include/KF6/KFileMetaData/KFileMetaData/ExtractorPlugin
/usr/include/KF6/KFileMetaData/KFileMetaData/MimeUtils
/usr/include/KF6/KFileMetaData/KFileMetaData/Properties
/usr/include/KF6/KFileMetaData/KFileMetaData/PropertyInfo
/usr/include/KF6/KFileMetaData/KFileMetaData/SimpleExtractionResult
/usr/include/KF6/KFileMetaData/KFileMetaData/TypeInfo
/usr/include/KF6/KFileMetaData/KFileMetaData/Types
/usr/include/KF6/KFileMetaData/KFileMetaData/UserMetaData
/usr/include/KF6/KFileMetaData/KFileMetaData/WriteData
/usr/include/KF6/KFileMetaData/KFileMetaData/Writer
/usr/include/KF6/KFileMetaData/KFileMetaData/WriterCollection
/usr/include/KF6/KFileMetaData/KFileMetaData/WriterPlugin
/usr/include/KF6/KFileMetaData/kfilemetadata/embeddedimagedata.h
/usr/include/KF6/KFileMetaData/kfilemetadata/extractionresult.h
/usr/include/KF6/KFileMetaData/kfilemetadata/extractor.h
/usr/include/KF6/KFileMetaData/kfilemetadata/extractorcollection.h
/usr/include/KF6/KFileMetaData/kfilemetadata/extractorplugin.h
/usr/include/KF6/KFileMetaData/kfilemetadata/kfilemetadata_export.h
/usr/include/KF6/KFileMetaData/kfilemetadata/mimeutils.h
/usr/include/KF6/KFileMetaData/kfilemetadata/properties.h
/usr/include/KF6/KFileMetaData/kfilemetadata/propertyinfo.h
/usr/include/KF6/KFileMetaData/kfilemetadata/simpleextractionresult.h
/usr/include/KF6/KFileMetaData/kfilemetadata/typeinfo.h
/usr/include/KF6/KFileMetaData/kfilemetadata/types.h
/usr/include/KF6/KFileMetaData/kfilemetadata/usermetadata.h
/usr/include/KF6/KFileMetaData/kfilemetadata/writedata.h
/usr/include/KF6/KFileMetaData/kfilemetadata/writer.h
/usr/include/KF6/KFileMetaData/kfilemetadata/writercollection.h
/usr/include/KF6/KFileMetaData/kfilemetadata/writerplugin.h
/usr/include/KF6/KFileMetaData/kfilemetadata_version.h
/usr/lib64/cmake/KF6FileMetaData/KF6FileMetaDataConfig.cmake
/usr/lib64/cmake/KF6FileMetaData/KF6FileMetaDataConfigVersion.cmake
/usr/lib64/cmake/KF6FileMetaData/KF6FileMetaDataTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6FileMetaData/KF6FileMetaDataTargets.cmake
/usr/lib64/libKF6FileMetaData.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6FileMetaData.so.6.6.0
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_exiv2extractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_fb2extractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_ffmpegextractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_krita.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_odfextractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_office2007extractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_officeextractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_plaintextextractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_pngextractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_poextractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_popplerextractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_postscriptdscextractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_taglibextractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_xmlextractor.so
/V3/usr/lib64/qt6/plugins/kf6/kfilemetadata/writers/kfilemetadata_taglibwriter.so
/usr/lib64/libKF6FileMetaData.so.3
/usr/lib64/libKF6FileMetaData.so.6.6.0
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_exiv2extractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_fb2extractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_ffmpegextractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_krita.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_odfextractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_office2007extractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_officeextractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_plaintextextractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_pngextractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_poextractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_popplerextractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_postscriptdscextractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_taglibextractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/kfilemetadata_xmlextractor.so
/usr/lib64/qt6/plugins/kf6/kfilemetadata/writers/kfilemetadata_taglibwriter.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kfilemetadata/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kfilemetadata/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kfilemetadata/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kfilemetadata/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kfilemetadata/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kfilemetadata/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kfilemetadata6.lang
%defattr(-,root,root,-)

