# Meta Package
Name:           ros-humble-moveit-resources-fanuc-description
Version:        2.0.7
Release:        1%{?dist}
License:        BSD
URL:            http://moveit.ros.org
Summary:        Meta package for ros2-humble-moveit_resources_fanuc_description and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-moveit_resources_fanuc_description
Requires:       ros2-humble-moveit_resources_fanuc_description-devel

Obsoletes: ros-humble-moveit-resources-fanuc-description < 2.0.7-1

%description
Fanuc Resources used for MoveIt testing

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 25 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.7-1
- Update to latest release
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.6-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.6-1
- Initial humble build
