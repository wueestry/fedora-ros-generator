# Meta Package
Name:           ros-iron-rviz-visual-testing-framework
Version:        12.4.7
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/rviz2
Summary:        Meta package for ros2-iron-rviz_visual_testing_framework and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rviz_visual_testing_framework
Requires:       ros2-iron-rviz_visual_testing_framework-devel

Obsoletes: ros-iron-rviz-visual-testing-framework < 12.4.7-1

%description
3D testing framework for RViz.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.12.4.7-1
- Update to latest release
