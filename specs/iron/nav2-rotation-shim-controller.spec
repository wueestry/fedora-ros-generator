# Meta Package
Name:           ros-iron-nav2-rotation-shim-controller
Version:        1.2.7
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-nav2_rotation_shim_controller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-nav2_rotation_shim_controller
Requires:       ros2-iron-nav2_rotation_shim_controller-devel

Obsoletes: ros-iron-nav2-rotation-shim-controller < 1.2.7-1

%description
Rotation Shim Controller

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
