# Meta Package
Name:           ros-jazzy-nav2-amcl
Version:        1.3.2
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-nav2_amcl and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-nav2_amcl
Requires:       ros2-jazzy-nav2_amcl-devel

Obsoletes: ros-jazzy-nav2-amcl < 1.3.2-1

%description
ROS jazzy package nav2_amcl.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.2-1
- Update to latest release
* Mon Jul 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-3
- Fix racecondition crash
* Mon Jul 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-2
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-1
- Update to latest release
