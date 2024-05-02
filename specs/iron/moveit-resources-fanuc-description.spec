# Meta Package
Name:           ros-iron-moveit-resources-fanuc-description
Version:        2.1.1
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-iron-moveit_resources_fanuc_description and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-moveit_resources_fanuc_description
Requires:       ros2-iron-moveit_resources_fanuc_description-devel

Obsoletes: ros-iron-moveit-resources-fanuc-description < 2.1.1-1

%description
Fanuc Resources used for MoveIt testing

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.1.1-1
- Update to latest release
