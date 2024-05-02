# Meta Package
Name:           ros-humble-sensor-msgs-py
Version:        4.2.3
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-sensor_msgs_py and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-sensor_msgs_py
Requires:       ros2-humble-sensor_msgs_py-devel

Obsoletes: ros-humble-sensor-msgs-py < 4.2.3-1

%description
A package for easy creation and reading of PointCloud2 messages in
Python.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.2.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.2.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.2.3-1
- Initial humble build
