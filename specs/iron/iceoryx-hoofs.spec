# Meta Package
Name:           ros-iron-iceoryx-hoofs
Version:        2.0.5
Release:        1%{?dist}
License:        Apache 2.0
URL:            https://iceoryx.io
Summary:        Meta package for ros2-iron-iceoryx_hoofs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-iceoryx_hoofs
Requires:       ros2-iron-iceoryx_hoofs-devel

Obsoletes: ros-iron-iceoryx-hoofs < 2.0.5-1

%description
Eclipse iceoryx inter-process-communication (IPC) middleware basic
building blocks

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.5-1
- Update to latest release
