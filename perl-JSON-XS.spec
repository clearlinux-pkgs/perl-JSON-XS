#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-JSON-XS
Version  : 4.03
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/JSON-XS-4.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/JSON-XS-4.03.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-JSON-XS-bin = %{version}-%{release}
Requires: perl-JSON-XS-license = %{version}-%{release}
Requires: perl-JSON-XS-man = %{version}-%{release}
Requires: perl-JSON-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Canary::Stability)
BuildRequires : perl(Types::Serialiser)
BuildRequires : perl(common::sense)

%description
NAME
JSON::XS - JSON serialising/deserialising, done correctly and fast
JSON::XS - 正しくて高速な JSON シリアライザ/デシリアライザ
(http://fleur.hio.jp/perldoc/mix/lib/JSON/XS.html)

%package bin
Summary: bin components for the perl-JSON-XS package.
Group: Binaries
Requires: perl-JSON-XS-license = %{version}-%{release}

%description bin
bin components for the perl-JSON-XS package.


%package dev
Summary: dev components for the perl-JSON-XS package.
Group: Development
Requires: perl-JSON-XS-bin = %{version}-%{release}
Provides: perl-JSON-XS-devel = %{version}-%{release}
Requires: perl-JSON-XS = %{version}-%{release}

%description dev
dev components for the perl-JSON-XS package.


%package license
Summary: license components for the perl-JSON-XS package.
Group: Default

%description license
license components for the perl-JSON-XS package.


%package man
Summary: man components for the perl-JSON-XS package.
Group: Default

%description man
man components for the perl-JSON-XS package.


%package perl
Summary: perl components for the perl-JSON-XS package.
Group: Default
Requires: perl-JSON-XS = %{version}-%{release}

%description perl
perl components for the perl-JSON-XS package.


%prep
%setup -q -n JSON-XS-4.03
cd %{_builddir}/JSON-XS-4.03

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-JSON-XS
cp %{_builddir}/JSON-XS-4.03/COPYING %{buildroot}/usr/share/package-licenses/perl-JSON-XS/9a56f3b919dfc8fced3803e165a2e38de62646e5
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/json_xs

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/JSON::XS.3
/usr/share/man/man3/JSON::XS::Boolean.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-JSON-XS/9a56f3b919dfc8fced3803e165a2e38de62646e5

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/json_xs.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/JSON/XS.pm
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/JSON/XS/Boolean.pm
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/JSON/XS/XS.so
