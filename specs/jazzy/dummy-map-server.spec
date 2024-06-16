# Meta Package
Name:           ros-jazzy-dummy-map-server
Version:        0.33.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-dummy_map_server and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-dummy_map_server
Requires:       ros2-jazzy-dummy_map_server-devel

Obsoletes: ros-jazzy-dummy-map-server < 0.33.3-1

%description
dummy map server node

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.2-1
- Update to latest release
