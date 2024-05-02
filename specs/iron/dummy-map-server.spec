# Meta Package
Name:           ros-iron-dummy-map-server
Version:        0.27.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-dummy_map_server and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-dummy_map_server
Requires:       ros2-iron-dummy_map_server-devel

Obsoletes: ros-iron-dummy-map-server < 0.27.1-1

%description
dummy map server node

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.27.1-1
- Update to latest release
