#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kfilemetadata
Version  : 5.69.0
Release  : 33
URL      : https://download.kde.org/stable/frameworks/5.69/kfilemetadata-5.69.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.69/kfilemetadata-5.69.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.69/kfilemetadata-5.69.0.tar.xz.sig
Summary  : A library for extracting file metadata
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kfilemetadata-data = %{version}-%{release}
Requires: kfilemetadata-lib = %{version}-%{release}
Requires: kfilemetadata-license = %{version}-%{release}
Requires: kfilemetadata-locales = %{version}-%{release}
BuildRequires : attr-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(poppler)
BuildRequires : ki18n-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libavformat)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libswscale)
BuildRequires : poppler-dev
BuildRequires : python3
BuildRequires : qtbase-dev mesa-dev
BuildRequires : taglib-dev

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
%setup -q -n kfilemetadata-5.69.0
cd %{_builddir}/kfilemetadata-5.69.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586875507
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
export SOURCE_DATE_EPOCH=1586875507
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kfilemetadata
cp %{_builddir}/kfilemetadata-5.69.0/COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/kfilemetadata/ba8966e2473a9969bdcab3dc82274c817cfd98a1
cp %{_builddir}/kfilemetadata-5.69.0/COPYING.LGPL-2.1 %{buildroot}/usr/share/package-licenses/kfilemetadata/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/kfilemetadata-5.69.0/COPYING.LGPL-3 %{buildroot}/usr/share/package-licenses/kfilemetadata/f45ee1c765646813b442ca58de72e20a64a7ddba
pushd clr-build
%make_install
popd
%find_lang kfilemetadata5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kfilemetadata.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KFileMetaData/KFileMetaData/EmbeddedImageData
/usr/include/KF5/KFileMetaData/KFileMetaData/ExtractionResult
/usr/include/KF5/KFileMetaData/KFileMetaData/Extractor
/usr/include/KF5/KFileMetaData/KFileMetaData/ExtractorCollection
/usr/include/KF5/KFileMetaData/KFileMetaData/ExtractorPlugin
/usr/include/KF5/KFileMetaData/KFileMetaData/MimeUtils
/usr/include/KF5/KFileMetaData/KFileMetaData/Properties
/usr/include/KF5/KFileMetaData/KFileMetaData/PropertyInfo
/usr/include/KF5/KFileMetaData/KFileMetaData/SimpleExtractionResult
/usr/include/KF5/KFileMetaData/KFileMetaData/TypeInfo
/usr/include/KF5/KFileMetaData/KFileMetaData/Types
/usr/include/KF5/KFileMetaData/KFileMetaData/UserMetaData
/usr/include/KF5/KFileMetaData/KFileMetaData/WriteData
/usr/include/KF5/KFileMetaData/KFileMetaData/Writer
/usr/include/KF5/KFileMetaData/KFileMetaData/WriterCollection
/usr/include/KF5/KFileMetaData/KFileMetaData/WriterPlugin
/usr/include/KF5/KFileMetaData/kfilemetadata/embeddedimagedata.h
/usr/include/KF5/KFileMetaData/kfilemetadata/extractionresult.h
/usr/include/KF5/KFileMetaData/kfilemetadata/extractor.h
/usr/include/KF5/KFileMetaData/kfilemetadata/extractorcollection.h
/usr/include/KF5/KFileMetaData/kfilemetadata/extractorplugin.h
/usr/include/KF5/KFileMetaData/kfilemetadata/kfilemetadata_export.h
/usr/include/KF5/KFileMetaData/kfilemetadata/mimeutils.h
/usr/include/KF5/KFileMetaData/kfilemetadata/properties.h
/usr/include/KF5/KFileMetaData/kfilemetadata/propertyinfo.h
/usr/include/KF5/KFileMetaData/kfilemetadata/simpleextractionresult.h
/usr/include/KF5/KFileMetaData/kfilemetadata/typeinfo.h
/usr/include/KF5/KFileMetaData/kfilemetadata/types.h
/usr/include/KF5/KFileMetaData/kfilemetadata/usermetadata.h
/usr/include/KF5/KFileMetaData/kfilemetadata/writedata.h
/usr/include/KF5/KFileMetaData/kfilemetadata/writer.h
/usr/include/KF5/KFileMetaData/kfilemetadata/writercollection.h
/usr/include/KF5/KFileMetaData/kfilemetadata/writerplugin.h
/usr/lib64/cmake/KF5FileMetaData/KF5FileMetaDataConfig.cmake
/usr/lib64/cmake/KF5FileMetaData/KF5FileMetaDataConfigVersion.cmake
/usr/lib64/cmake/KF5FileMetaData/KF5FileMetaDataTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5FileMetaData/KF5FileMetaDataTargets.cmake
/usr/lib64/libKF5FileMetaData.so
/usr/lib64/qt5/mkspecs/modules/qt_KFileMetaData.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5FileMetaData.so.3
/usr/lib64/libKF5FileMetaData.so.5.69.0
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_ffmpegextractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_odfextractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_office2007extractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_officeextractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_plaintextextractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_poextractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_popplerextractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_postscriptdscextractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_taglibextractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_xmlextractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/writers/kfilemetadata_taglibwriter.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kfilemetadata/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/kfilemetadata/ba8966e2473a9969bdcab3dc82274c817cfd98a1
/usr/share/package-licenses/kfilemetadata/f45ee1c765646813b442ca58de72e20a64a7ddba

%files locales -f kfilemetadata5.lang
%defattr(-,root,root,-)

