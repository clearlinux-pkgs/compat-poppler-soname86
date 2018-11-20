#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3A6A4DB839EAA6D7 (aacid@kde.org)
#
Name     : poppler
Version  : 0.71.0
Release  : 25
URL      : https://poppler.freedesktop.org/poppler-0.71.0.tar.xz
Source0  : https://poppler.freedesktop.org/poppler-0.71.0.tar.xz
Source99 : https://poppler.freedesktop.org/poppler-0.71.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0
Requires: poppler-bin = %{version}-%{release}
Requires: poppler-data = %{version}-%{release}
Requires: poppler-lib = %{version}-%{release}
Requires: poppler-license = %{version}-%{release}
Requires: poppler-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : curl-dev
BuildRequires : freetype-dev
BuildRequires : glibc-bin
BuildRequires : glibc-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(cairo-pdf)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(nss)
BuildRequires : qtbase-extras
BuildRequires : tiff-dev
BuildRequires : zlib-dev

%description
This is poppler, a PDF rendering library.
Poppler is a fork of the xpdf PDF viewer developed by Derek Noonburg
of Glyph and Cog, LLC.  The purpose of forking xpdf is twofold.
First, we want to provide PDF rendering functionality as a shared
library, to centralize the maintenance effort.  Today a number of
applications incorporate the xpdf code base, and whenever a security
issue is discovered, all these applications exchange patches and put
out new releases.  In turn, all distributions must package and release
new version of these xpdf based viewers.  It's safe to say that
there's a lot of duplicated effort with the current situation.  Even if
poppler in the short term introduces yet another xpdf derived code
base to the world, we hope that over time these applications will
adopt poppler.  After all, we only need one application to use poppler
to break even.

%package bin
Summary: bin components for the poppler package.
Group: Binaries
Requires: poppler-data = %{version}-%{release}
Requires: poppler-license = %{version}-%{release}
Requires: poppler-man = %{version}-%{release}

%description bin
bin components for the poppler package.


%package data
Summary: data components for the poppler package.
Group: Data

%description data
data components for the poppler package.


%package dev
Summary: dev components for the poppler package.
Group: Development
Requires: poppler-lib = %{version}-%{release}
Requires: poppler-bin = %{version}-%{release}
Requires: poppler-data = %{version}-%{release}
Provides: poppler-devel = %{version}-%{release}

%description dev
dev components for the poppler package.


%package extras
Summary: extras components for the poppler package.
Group: Default

%description extras
extras components for the poppler package.


%package lib
Summary: lib components for the poppler package.
Group: Libraries
Requires: poppler-data = %{version}-%{release}
Requires: poppler-license = %{version}-%{release}

%description lib
lib components for the poppler package.


%package license
Summary: license components for the poppler package.
Group: Default

%description license
license components for the poppler package.


%package man
Summary: man components for the poppler package.
Group: Default

%description man
man components for the poppler package.


%prep
%setup -q -n poppler-0.71.0
pushd ..
cp -a poppler-0.71.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542752154
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%cmake .. -DENABLE_XPDF_HEADERS=ON -DENABLE_UTILS=ON -DENABLE_LIBOPENJPEG=none
make  %{?_smp_mflags} VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell -mzero-caller-saved-regs=used "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake .. -DENABLE_XPDF_HEADERS=ON -DENABLE_UTILS=ON -DENABLE_LIBOPENJPEG=none
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1542752154
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/poppler
cp COPYING %{buildroot}/usr/share/package-licenses/poppler/COPYING
cp COPYING3 %{buildroot}/usr/share/package-licenses/poppler/COPYING3
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/poppler/cmake_modules_COPYING-CMAKE-SCRIPTS
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/haswell/pdfdetach
/usr/bin/haswell/pdffonts
/usr/bin/haswell/pdfimages
/usr/bin/haswell/pdfinfo
/usr/bin/haswell/pdfseparate
/usr/bin/haswell/pdfsig
/usr/bin/haswell/pdftocairo
/usr/bin/haswell/pdftohtml
/usr/bin/haswell/pdftoppm
/usr/bin/haswell/pdftops
/usr/bin/haswell/pdftotext
/usr/bin/haswell/pdfunite
/usr/bin/pdfdetach
/usr/bin/pdffonts
/usr/bin/pdfimages
/usr/bin/pdfinfo
/usr/bin/pdfseparate
/usr/bin/pdfsig
/usr/bin/pdftocairo
/usr/bin/pdftohtml
/usr/bin/pdftoppm
/usr/bin/pdftops
/usr/bin/pdftotext
/usr/bin/pdfunite

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Poppler-0.18.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/poppler/qt5/poppler-annotation.h
%exclude /usr/include/poppler/qt5/poppler-export.h
%exclude /usr/include/poppler/qt5/poppler-form.h
%exclude /usr/include/poppler/qt5/poppler-link.h
%exclude /usr/include/poppler/qt5/poppler-media.h
%exclude /usr/include/poppler/qt5/poppler-optcontent.h
%exclude /usr/include/poppler/qt5/poppler-page-transition.h
%exclude /usr/include/poppler/qt5/poppler-qt5.h
%exclude /usr/lib64/haswell/libpoppler-qt5.so
%exclude /usr/lib64/libpoppler-qt5.so
%exclude /usr/lib64/pkgconfig/poppler-qt5.pc
/usr/include/poppler/Annot.h
/usr/include/poppler/Array.h
/usr/include/poppler/BuiltinFont.h
/usr/include/poppler/BuiltinFontTables.h
/usr/include/poppler/CMap.h
/usr/include/poppler/CachedFile.h
/usr/include/poppler/Catalog.h
/usr/include/poppler/CharCodeToUnicode.h
/usr/include/poppler/CharTypes.h
/usr/include/poppler/CompactFontTables.h
/usr/include/poppler/CurlCachedFile.h
/usr/include/poppler/CurlPDFDocBuilder.h
/usr/include/poppler/DateInfo.h
/usr/include/poppler/Decrypt.h
/usr/include/poppler/Dict.h
/usr/include/poppler/Error.h
/usr/include/poppler/ErrorCodes.h
/usr/include/poppler/FileSpec.h
/usr/include/poppler/FontEncodingTables.h
/usr/include/poppler/FontInfo.h
/usr/include/poppler/Form.h
/usr/include/poppler/Function.h
/usr/include/poppler/Gfx.h
/usr/include/poppler/GfxFont.h
/usr/include/poppler/GfxState.h
/usr/include/poppler/GfxState_helpers.h
/usr/include/poppler/GlobalParams.h
/usr/include/poppler/Hints.h
/usr/include/poppler/JArithmeticDecoder.h
/usr/include/poppler/JBIG2Stream.h
/usr/include/poppler/JPXStream.h
/usr/include/poppler/Lexer.h
/usr/include/poppler/Linearization.h
/usr/include/poppler/Link.h
/usr/include/poppler/LocalPDFDocBuilder.h
/usr/include/poppler/MarkedContentOutputDev.h
/usr/include/poppler/Movie.h
/usr/include/poppler/NameToCharCode.h
/usr/include/poppler/NameToUnicodeTable.h
/usr/include/poppler/Object.h
/usr/include/poppler/OptionalContent.h
/usr/include/poppler/Outline.h
/usr/include/poppler/OutputDev.h
/usr/include/poppler/PDFDoc.h
/usr/include/poppler/PDFDocBuilder.h
/usr/include/poppler/PDFDocEncoding.h
/usr/include/poppler/PDFDocFactory.h
/usr/include/poppler/PSOutputDev.h
/usr/include/poppler/PSTokenizer.h
/usr/include/poppler/Page.h
/usr/include/poppler/PageTransition.h
/usr/include/poppler/Parser.h
/usr/include/poppler/PopplerCache.h
/usr/include/poppler/PreScanOutputDev.h
/usr/include/poppler/ProfileData.h
/usr/include/poppler/Rendition.h
/usr/include/poppler/SecurityHandler.h
/usr/include/poppler/Sound.h
/usr/include/poppler/SplashOutputDev.h
/usr/include/poppler/StdinCachedFile.h
/usr/include/poppler/StdinPDFDocBuilder.h
/usr/include/poppler/Stream-CCITT.h
/usr/include/poppler/Stream.h
/usr/include/poppler/StructElement.h
/usr/include/poppler/StructTreeRoot.h
/usr/include/poppler/TextOutputDev.h
/usr/include/poppler/UTF.h
/usr/include/poppler/UnicodeCClassTables.h
/usr/include/poppler/UnicodeCompTables.h
/usr/include/poppler/UnicodeDecompTables.h
/usr/include/poppler/UnicodeMap.h
/usr/include/poppler/UnicodeMapFuncs.h
/usr/include/poppler/UnicodeMapTables.h
/usr/include/poppler/UnicodeTypeTable.h
/usr/include/poppler/ViewerPreferences.h
/usr/include/poppler/XRef.h
/usr/include/poppler/cpp/poppler-document.h
/usr/include/poppler/cpp/poppler-embedded-file.h
/usr/include/poppler/cpp/poppler-font.h
/usr/include/poppler/cpp/poppler-global.h
/usr/include/poppler/cpp/poppler-image.h
/usr/include/poppler/cpp/poppler-page-renderer.h
/usr/include/poppler/cpp/poppler-page-transition.h
/usr/include/poppler/cpp/poppler-page.h
/usr/include/poppler/cpp/poppler-rectangle.h
/usr/include/poppler/cpp/poppler-toc.h
/usr/include/poppler/cpp/poppler-version.h
/usr/include/poppler/fofi/FoFiBase.h
/usr/include/poppler/fofi/FoFiEncodings.h
/usr/include/poppler/fofi/FoFiIdentifier.h
/usr/include/poppler/fofi/FoFiTrueType.h
/usr/include/poppler/fofi/FoFiType1.h
/usr/include/poppler/fofi/FoFiType1C.h
/usr/include/poppler/glib/poppler-action.h
/usr/include/poppler/glib/poppler-annot.h
/usr/include/poppler/glib/poppler-attachment.h
/usr/include/poppler/glib/poppler-date.h
/usr/include/poppler/glib/poppler-document.h
/usr/include/poppler/glib/poppler-enums.h
/usr/include/poppler/glib/poppler-features.h
/usr/include/poppler/glib/poppler-form-field.h
/usr/include/poppler/glib/poppler-layer.h
/usr/include/poppler/glib/poppler-macros.h
/usr/include/poppler/glib/poppler-media.h
/usr/include/poppler/glib/poppler-movie.h
/usr/include/poppler/glib/poppler-page.h
/usr/include/poppler/glib/poppler-structure-element.h
/usr/include/poppler/glib/poppler.h
/usr/include/poppler/goo/FixedPoint.h
/usr/include/poppler/goo/GooCheckedOps.h
/usr/include/poppler/goo/GooLikely.h
/usr/include/poppler/goo/GooList.h
/usr/include/poppler/goo/GooString.h
/usr/include/poppler/goo/GooTimer.h
/usr/include/poppler/goo/ImgWriter.h
/usr/include/poppler/goo/JpegWriter.h
/usr/include/poppler/goo/PNGWriter.h
/usr/include/poppler/goo/TiffWriter.h
/usr/include/poppler/goo/gdir.h
/usr/include/poppler/goo/gfile.h
/usr/include/poppler/goo/gmem.h
/usr/include/poppler/goo/grandom.h
/usr/include/poppler/goo/gstrtod.h
/usr/include/poppler/goo/gtypes.h
/usr/include/poppler/poppler-config.h
/usr/include/poppler/splash/Splash.h
/usr/include/poppler/splash/SplashBitmap.h
/usr/include/poppler/splash/SplashClip.h
/usr/include/poppler/splash/SplashErrorCodes.h
/usr/include/poppler/splash/SplashFTFont.h
/usr/include/poppler/splash/SplashFTFontEngine.h
/usr/include/poppler/splash/SplashFTFontFile.h
/usr/include/poppler/splash/SplashFont.h
/usr/include/poppler/splash/SplashFontEngine.h
/usr/include/poppler/splash/SplashFontFile.h
/usr/include/poppler/splash/SplashFontFileID.h
/usr/include/poppler/splash/SplashGlyphBitmap.h
/usr/include/poppler/splash/SplashMath.h
/usr/include/poppler/splash/SplashPath.h
/usr/include/poppler/splash/SplashPattern.h
/usr/include/poppler/splash/SplashScreen.h
/usr/include/poppler/splash/SplashState.h
/usr/include/poppler/splash/SplashTypes.h
/usr/include/poppler/splash/SplashXPath.h
/usr/include/poppler/splash/SplashXPathScanner.h
/usr/lib64/haswell/libpoppler-cpp.so
/usr/lib64/haswell/libpoppler-glib.so
/usr/lib64/haswell/libpoppler.so
/usr/lib64/libpoppler-cpp.so
/usr/lib64/libpoppler-glib.so
/usr/lib64/libpoppler.so
/usr/lib64/pkgconfig/poppler-cairo.pc
/usr/lib64/pkgconfig/poppler-cpp.pc
/usr/lib64/pkgconfig/poppler-glib.pc
/usr/lib64/pkgconfig/poppler-splash.pc
/usr/lib64/pkgconfig/poppler.pc

%files extras
%defattr(-,root,root,-)
/usr/include/poppler/qt5/poppler-annotation.h
/usr/include/poppler/qt5/poppler-export.h
/usr/include/poppler/qt5/poppler-form.h
/usr/include/poppler/qt5/poppler-link.h
/usr/include/poppler/qt5/poppler-media.h
/usr/include/poppler/qt5/poppler-optcontent.h
/usr/include/poppler/qt5/poppler-page-transition.h
/usr/include/poppler/qt5/poppler-qt5.h
/usr/lib64/haswell/libpoppler-qt5.so
/usr/lib64/haswell/libpoppler-qt5.so.1
/usr/lib64/libpoppler-qt5.so
/usr/lib64/libpoppler-qt5.so.1
/usr/lib64/pkgconfig/poppler-qt5.pc

%files lib
%defattr(-,root,root,-)
%exclude /usr/lib64/haswell/libpoppler-qt5.so.1
%exclude /usr/lib64/libpoppler-qt5.so.1
/usr/lib64/haswell/libpoppler-cpp.so.0
/usr/lib64/haswell/libpoppler-cpp.so.0.5.0
/usr/lib64/haswell/libpoppler-glib.so.8
/usr/lib64/haswell/libpoppler-glib.so.8.10.0
/usr/lib64/haswell/libpoppler-qt5.so.1.17.0
/usr/lib64/haswell/libpoppler.so.82
/usr/lib64/haswell/libpoppler.so.82.0.0
/usr/lib64/libpoppler-cpp.so.0
/usr/lib64/libpoppler-cpp.so.0.5.0
/usr/lib64/libpoppler-glib.so.8
/usr/lib64/libpoppler-glib.so.8.10.0
/usr/lib64/libpoppler-qt5.so.1.17.0
/usr/lib64/libpoppler.so.82
/usr/lib64/libpoppler.so.82.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/poppler/COPYING
/usr/share/package-licenses/poppler/COPYING3
/usr/share/package-licenses/poppler/cmake_modules_COPYING-CMAKE-SCRIPTS

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pdfdetach.1
/usr/share/man/man1/pdffonts.1
/usr/share/man/man1/pdfimages.1
/usr/share/man/man1/pdfinfo.1
/usr/share/man/man1/pdfseparate.1
/usr/share/man/man1/pdfsig.1
/usr/share/man/man1/pdftocairo.1
/usr/share/man/man1/pdftohtml.1
/usr/share/man/man1/pdftoppm.1
/usr/share/man/man1/pdftops.1
/usr/share/man/man1/pdftotext.1
/usr/share/man/man1/pdfunite.1
