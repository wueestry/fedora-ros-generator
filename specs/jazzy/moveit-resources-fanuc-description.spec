# Meta Package
Name:           ros-jazzy-moveit-resources-fanuc-description
Version:        3.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-jazzy-moveit_resources_fanuc_description and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-moveit_resources_fanuc_description
Requires:       ros2-jazzy-moveit_resources_fanuc_description-devel

Obsoletes: ros-jazzy-moveit-resources-fanuc-description < 3.0.0-1

%description
Fanuc Resources used for MoveIt testing

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.0.0-1
- Update to latest release
