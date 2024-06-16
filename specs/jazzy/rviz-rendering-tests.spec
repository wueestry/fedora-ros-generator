# Meta Package
Name:           ros-jazzy-rviz-rendering-tests
Version:        14.1.1
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rviz_rendering_tests and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rviz_rendering_tests
Requires:       ros2-jazzy-rviz_rendering_tests-devel

Obsoletes: ros-jazzy-rviz-rendering-tests < 14.1.1-1

%description
Example plugin for RViz - documents and tests RViz plugin development

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.0-1
- Update to latest release
