# Meta Package
Name:           ros-humble-pid-controller
Version:        2.37.0
Release:        1%{?dist}
License:        Apache-2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-pid_controller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-pid_controller
Requires:       ros2-humble-pid_controller-devel

Obsoletes: ros-humble-pid-controller < 2.37.0-1

%description
Controller based on PID implememenation from control_toolbox package.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.37.0-1
- Update to latest release
