#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kfilemetadata
Version  : 5.48.0
Release  : 2
URL      : https://download.kde.org/stable/frameworks/5.48/kfilemetadata-5.48.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.48/kfilemetadata-5.48.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.48/kfilemetadata-5.48.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kfilemetadata-lib
Requires: kfilemetadata-license
Requires: kfilemetadata-locales
BuildRequires : attr-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : exiv2-dev
BuildRequires : karchive-dev
BuildRequires : ki18n-dev
BuildRequires : poppler-dev

%description
This folder contains various small files to be indexed by indexerextractortests.

%package dev
Summary: dev components for the kfilemetadata package.
Group: Development
Requires: kfilemetadata-lib
Provides: kfilemetadata-devel

%description dev
dev components for the kfilemetadata package.


%package lib
Summary: lib components for the kfilemetadata package.
Group: Libraries
Requires: kfilemetadata-license

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
%setup -q -n kfilemetadata-5.48.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531926251
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1531926251
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kfilemetadata
cp COPYING.LGPL-3 %{buildroot}/usr/share/doc/kfilemetadata/COPYING.LGPL-3
cp COPYING.LGPL-2.1 %{buildroot}/usr/share/doc/kfilemetadata/COPYING.LGPL-2.1
cp COPYING.LGPL-2 %{buildroot}/usr/share/doc/kfilemetadata/COPYING.LGPL-2
pushd clr-build
%make_install
popd
%find_lang kfilemetadata5

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KFileMetaData/KFileMetaData/EmbeddedImageData
/usr/include/KF5/KFileMetaData/KFileMetaData/ExtractionResult
/usr/include/KF5/KFileMetaData/KFileMetaData/Extractor
/usr/include/KF5/KFileMetaData/KFileMetaData/ExtractorCollection
/usr/include/KF5/KFileMetaData/KFileMetaData/ExtractorPlugin
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
/usr/lib64/libKF5FileMetaData.so.5.48.0
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_exiv2extractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_odfextractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_office2007extractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_officeextractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_plaintextextractor.so
/usr/lib64/qt5/plugins/kf5/kfilemetadata/kfilemetadata_poextractor.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/kfilemetadata/COPYING.LGPL-2
/usr/share/doc/kfilemetadata/COPYING.LGPL-2.1
/usr/share/doc/kfilemetadata/COPYING.LGPL-3

%files locales -f kfilemetadata5.lang
%defattr(-,root,root,-)

