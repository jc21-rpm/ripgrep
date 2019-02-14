%global debug_package %{nil}

Name:           ripgrep
Version:        0.10.0
Release:        1%{?dist}
Summary:        ripgrep recursively searches directories for a regex pattern
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/BurnSushi/%{name}
BuildRequires:  cmake
%{?el7:BuildRequires: cargo, rust}

%description
ripgrep is a line-oriented search tool that recursively searches your current
directory for a regex pattern while respecting your gitignore rules. ripgrep
has first class support on Windows, macOS and Linux, with binary downloads
available for every release. ripgrep is similar to other popular search tools
like The Silver Searcher, ack and grep.

%prep
wget https://github.com/BurntSushi/%{name}/archive/%{version}.tar.gz
tar xzf %{version}.tar.gz


%build
cd %{name}-%{version}
cargo build --release


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
install -D -m 755 %{name}-%{version}/target/release/rg %{buildroot}/usr/bin/rg


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc %{name}-%{version}/LICENSE-MIT %{name}-%{version}/*.md
/usr/bin/rg


%changelog
* Tue Sep 11 2018 Jamie Curnow <jc@jc21.com> - 0.10.0-1
- 0.10.1

* Fri Aug 31 2018 Jamie Curnow <jc@jc21.com> - 0.9.0-1
- Initial spec

