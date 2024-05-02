# Meta Package
Name:           ros-humble-webots-ros2-importer
Version:        2023.1.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://wiki.ros.org/webots_ros2
Summary:        Meta package for ros2-humble-webots_ros2_importer and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-webots_ros2_importer
Requires:       ros2-humble-webots_ros2_importer-devel

Obsoletes: ros-humble-webots-ros2-importer < 2023.1.2-1

%description
This package allows to convert URDF and XACRO files into Webots PROTO
files.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 09 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2023.1.2-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2023.1.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2023.1.1-1
- update to latest upstream release
* Fri Aug 11 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2023.1.1-1
- update to latest upstream
* Sat Jul 01 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2023.1.0-1
- update to latest upstream release
* Sat Apr 15 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2023.0.3-1
- update to latest release
