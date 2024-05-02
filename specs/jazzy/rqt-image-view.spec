# Meta Package
Name:           ros-jazzy-rqt-image-view
Version:        1.3.0
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_image_view
Summary:        Meta package for ros2-jazzy-rqt_image_view and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_image_view
Requires:       ros2-jazzy-rqt_image_view-devel

Obsoletes: ros-jazzy-rqt-image-view < 1.3.0-1

%description
rqt_image_view provides a GUI plugin for displaying images using
image_transport.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.0-1
- Update to latest release
