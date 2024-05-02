# Meta Package
Name:           ros-humble-dummy-map-server
Version:        0.20.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-dummy_map_server and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-dummy_map_server
Requires:       ros2-humble-dummy_map_server-devel

Obsoletes: ros-humble-dummy-map-server < 0.20.3-1

%description
dummy map server node

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.20.3-1
- Initial humble build
