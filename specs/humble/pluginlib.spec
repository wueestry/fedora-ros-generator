# Meta Package
Name:           ros-humble-pluginlib
Version:        5.1.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-pluginlib and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-pluginlib
Requires:       ros2-humble-pluginlib-devel

Obsoletes: ros-humble-pluginlib < 5.1.0-1

%description
The pluginlib package provides tools for writing and dynamically
loading plugins using the ROS build infrastructure. To work, these
tools require plugin providers to register their plugins in the
package.xml of their package.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.1.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.1.0-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.1.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.13.0-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.5.1.0-1
- Initial humble build
