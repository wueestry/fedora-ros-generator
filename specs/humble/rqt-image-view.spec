# Meta Package
Name:           ros-humble-rqt-image-view
Version:        1.2.0
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_image_view
Summary:        Meta package for ros2-humble-rqt_image_view and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rqt_image_view
Requires:       ros2-humble-rqt_image_view-devel

Obsoletes: ros-humble-rqt-image-view < 1.2.0-1

%description
rqt_image_view provides a GUI plugin for displaying images using
image_transport.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.0.4.17-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.2.0-1
- Initial humble build
