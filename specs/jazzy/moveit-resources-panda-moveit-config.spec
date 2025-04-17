# Meta Package
Name:           ros-jazzy-moveit-resources-panda-moveit-config
Version:        3.1.0
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org/
Summary:        Meta package for ros2-jazzy-moveit_resources_panda_moveit_config and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_resources_panda_moveit_config
Requires:       ros2-jazzy-moveit_resources_panda_moveit_config-devel

Obsoletes: ros-jazzy-moveit-resources-panda-moveit-config < 3.1.0-1

%description
ROS jazzy package moveit_resources_panda_moveit_config.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.1.0-1
- Update to latest release
* Thu Nov 21 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.0.0-2
- Rebuild due to srdfdom update
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.0.0-1
- Update to latest release
