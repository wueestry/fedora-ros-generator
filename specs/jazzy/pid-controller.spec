# Meta Package
Name:           ros-jazzy-pid-controller
Version:        4.7.0
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-pid_controller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-pid_controller
Requires:       ros2-jazzy-pid_controller-devel

Obsoletes: ros-jazzy-pid-controller < 4.7.0-1

%description
Controller based on PID implememenation from control_toolbox package.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.7.0-1
- Update to latest release
