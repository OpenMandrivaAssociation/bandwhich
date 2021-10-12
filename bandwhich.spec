%global	debug_package %nil

Summary:	Terminal bandwidth utilization tool
Name:		bandwhich
Version:	0.20.0
Release:	2
License:	BSD
Group:		Text tools
Url:		https://github.com/imsnif/bandwhich
Source0:	https://github.com/imsnif/bandwhich/archive/%{version}.tar.gz
BuildRequires:	rust
BuildRequires:	cargo

%description
This is a CLI utility for displaying current network
utilization by process, connection and remote IP/hostname

%prep
%autosetup -p1

%build
cargo build --release --locked

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm 755 "target/release/%{name}" %{buildroot}%{_bindir}
install -Dm 644 "docs/bandwhich.1" -t "%{buildroot}/%{_mandir}/man1"

%check
cargo test --release --locked
%post
%{_sbindir}/setcap cap_net_raw,cap_net_admin=+ep %{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
