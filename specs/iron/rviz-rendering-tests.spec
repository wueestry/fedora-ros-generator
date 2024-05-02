# Meta Package
Name:           ros-iron-rviz-rendering-tests
Version:        12.4.7
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rviz_rendering_tests and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rviz_rendering_tests
Requires:       ros2-iron-rviz_rendering_tests-devel

Obsoletes: ros-iron-rviz-rendering-tests < 12.4.7-1

%description
Example plugin for RViz - documents and tests RViz plugin development

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.12.4.7-1
- Update to latest release
