%define _disable_lto 1

Name:		rhash
Version:	1.3.6
Release:	1
Summary:	Great utility for computing hash sums
Group:		System/Libraries
License:	MIT
URL:		https://github.com/rhash/RHash
Source0:	https://github.com/rhash/RHash/archive/v%{version}/RHash-%{version}.tar.gz
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(openssl)

%description
RHash is a console utility for calculation  and verification of magnet links
and a wide range of hash sums like  CRC32,  MD4, MD5,  SHA1, SHA256, SHA512,
SHA3,   AICH,  ED2K,  Tiger,  DC++ TTH,  BitTorrent BTIH,   GOST R 34.11-94,
RIPEMD-160, HAS-160, EDON-R, Whirlpool and Snefru.

Hash sums are used to  ensure and verify integrity  of large volumes of data
for a long-term storing or transferring.

Features:
 * Output in a predefined (SFV, BSD-like) or a user-defined format.
 * Can calculate Magnet links.
 * Updating hash files (adding hash sums of files missing in the hash file).
 * Calculates several hash sums in one pass
 * Ability to process directories recursively.
 * Portability: the program works the same on Linux, *BSD or Windows.

%libpackage rhash 0

%package devel
Summary:	Development files for lib%{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}
Requires:	%{mklibname rhash 0} = %{EVRD}

%description    devel
LibRHash is a professional,  portable,  thread-safe  C library for computing
a wide variety of hash sums, such as  CRC32, MD4, MD5, SHA1, SHA256, SHA512,
SHA3,   AICH,  ED2K,  Tiger,  DC++ TTH,  BitTorrent BTIH,   GOST R 34.11-94,
RIPEMD-160, HAS-160, EDON-R, Whirlpool and Snefru.
Hash sums are used  to ensure and verify integrity of  large volumes of data
for a long-term storing or transferring.

Features:
 * Small and easy to learn interface.
 * Hi-level and Low-level API.
 * Allows calculating of several hash functions simultaneously.
 * Portability: the library works on Linux, *BSD and Windows.

The %{name}-devel package contains libraries and header files for
developing applications that use lib%{name}.


%prep
%setup -q -n RHash-%{version}
sed -i -e '/^INSTALL_SHARED/s/644/755/' librhash/Makefile


%build
%setup_compile_flags
./configure --cc=%{__cc} --prefix=%{_prefix}
%make CC="%{__cc}" OPTFLAGS="%{optflags}" OPTLDFLAGS="-g %{ldflags}" build-shared

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} install-shared install-lib-shared
make DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} -C librhash install-so-link install-headers


%check
make test-shared

%files
%doc README COPYING
%config(noreplace) %{_sysconfdir}/rhashrc
%{_bindir}/*
%{_mandir}/man1/*.1*

%files devel
%{_includedir}/*
%{_libdir}/*.so
