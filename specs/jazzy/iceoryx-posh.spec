# Meta Package
Name:           ros-jazzy-iceoryx-posh
Version:        2.0.5
Release:        1%{?dist}
License:        Apache 2.0
URL:            https://iceoryx.io
Summary:        Meta package for ros2-jazzy-iceoryx_posh and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-iceoryx_posh
Requires:       ros2-jazzy-iceoryx_posh-devel

Obsoletes: ros-jazzy-iceoryx-posh < 2.0.5-1

%description
Eclipse iceoryx inter-process-communication (IPC) middleware Posix
Shared Memory Library and middleware daemon (RouDi)

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.5-1
- Update to latest release
