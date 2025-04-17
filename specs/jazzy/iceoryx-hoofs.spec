# Meta Package
Name:           ros-jazzy-iceoryx-hoofs
Version:        2.0.6
Release:        1%{?dist}
License:        Apache 2.0
URL:            https://iceoryx.io
Summary:        Meta package for ros2-jazzy-iceoryx_hoofs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-iceoryx_hoofs
Requires:       ros2-jazzy-iceoryx_hoofs-devel

Obsoletes: ros-jazzy-iceoryx-hoofs < 2.0.6-1

%description
Eclipse iceoryx inter-process-communication (IPC) middleware basic
building blocks

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.6-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.5-1
- Update to latest release
