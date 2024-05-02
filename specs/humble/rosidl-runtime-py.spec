# Meta Package
Name:           ros-humble-rosidl-runtime-py
Version:        0.9.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-rosidl_runtime_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rosidl_runtime_py
Requires:       ros2-humble-rosidl_runtime_py-devel

Obsoletes: ros-humble-rosidl-runtime-py < 0.9.3-1

%description
Runtime utilities for working with generated ROS interfaces in Python.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.9.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.9.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.9.3-1
- Initial humble build
