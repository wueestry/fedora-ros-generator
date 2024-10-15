# Meta Package
Name:           ros-jazzy-rviz-visual-testing-framework
Version:        14.1.2
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/rviz2
Summary:        Meta package for ros2-jazzy-rviz_visual_testing_framework and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rviz_visual_testing_framework
Requires:       ros2-jazzy-rviz_visual_testing_framework-devel

Obsoletes: ros-jazzy-rviz-visual-testing-framework < 14.1.2-1

%description
3D testing framework for RViz.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.2-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.14.1.0-1
- Update to latest release
