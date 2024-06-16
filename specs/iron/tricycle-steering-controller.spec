# Meta Package
Name:           ros-iron-tricycle-steering-controller
Version:        3.24.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-tricycle_steering_controller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tricycle_steering_controller
Requires:       ros2-iron-tricycle_steering_controller-devel

Obsoletes: ros-iron-tricycle-steering-controller < 3.24.0-1

%description
Steering controller with tricycle kinematics. Rear fixed wheels are
powering the vehicle and front wheel is steering.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.24.0-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.22.0-1
- Update to latest release
