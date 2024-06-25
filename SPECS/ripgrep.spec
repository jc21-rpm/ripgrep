%global debug_package %{nil}

Name:           ripgrep
Version:        14.1.0
Release:        1%{?dist}
Summary:        ripgrep recursively searches directories for a regex pattern
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/BurnSushi/%{name}
Source:         https://github.com/BurntSushi/%{name}/archive/%{version}.tar.gz
BuildRequires:  cmake
%{?el7:BuildRequires: cargo, rust}

%description
ripgrep is a line-oriented search tool that recursively searches your current
directory for a regex pattern while respecting your gitignore rules. ripgrep
has first class support on Windows, macOS and Linux, with binary downloads
available for every release. ripgrep is similar to other popular search tools
like The Silver Searcher, ack and grep.

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
install -D -m 755 target/release/rg %{buildroot}/usr/bin/rg

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE-MIT *.md
/usr/bin/rg

%changelog
* Tue Jun 25 2024 Jamie Curnow <jc@jc21.com> - 14.1.0-1
- v14.1.0

* Sun Jun 20 2021 Jamie Curnow <jc@jc21.com> - 13.0.0-1
- v13.0.0

* Fri Aug 2 2019 Jamie Curnow <jc@jc21.com> - 11.0.2-1
- v11.0.2

* Wed Apr 17 2019 Jamie Curnow <jc@jc21.com> - 11.0.1-1
- v11.0.1

* Tue Sep 11 2018 Jamie Curnow <jc@jc21.com> - 0.10.0-1
- 0.10.1

* Fri Aug 31 2018 Jamie Curnow <jc@jc21.com> - 0.9.0-1
- Initial spec

